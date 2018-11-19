/**
 * Max Goldberg and Alexis Engel.
 * This will allow the user to control the frog.
 */

package frogger;

import java.util.Timer;
import java.util.TimerTask;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Controller implements EventHandler<KeyEvent> {
  @FXML private Label messageLabel;
  @FXML private FroggerView froggerView;
  private FroggerModel froggerModel;

  private Timer timer;
  private boolean paused;
  private final double FRAMES_PER_SECOND = 60;
  private int tic = 0;

  public Controller() {
  }

  public void initialize() {
    this.paused = false;
    this.startTimer();
    this.froggerModel = new FroggerModel(this.froggerView.getRowCount(), this.froggerView.getColumnCount());
    this.update();
  }

  public double getBoardWidth() {
    return froggerView.CELL_WIDTH * this.froggerView.getColumnCount();
  }

  public double getBoardHeight() {
    return FroggerView.CELL_WIDTH * this.froggerView.getRowCount();
  }

  /**
   * Adds text to the screen.
   */
  public void update() {
    this.froggerView.update(this.froggerModel);
    if (tic%15 == 0) {
      this.froggerModel.updateAnimation();
    }
    tic++;
    if (this.froggerModel.isGameLost()) {
      this.messageLabel.setText("Game Over. Hit N to start a new game.");
    }
    else if(this.froggerModel.isGameWon()) {
      this.messageLabel.setText("Game Won!!!!! Hit N to start a new game.");
    }
    else {
      this.messageLabel.setText("Get to all four lilypads without dying!");
    }
  }

  /**
   * Controls the frogger with key inputs. Also allows the user to quit, start over, or pause.
   */
  @Override
  public void handle(KeyEvent keyEvent) {
    boolean keyRecognized = true;
    KeyCode code = keyEvent.getCode();

    String s = code.getChar();
    if (s.length() > 0) {
      char theCharacterWeWant = s.charAt(0);
    }
    if (code == KeyCode.LEFT || code == KeyCode.A) {
      this.froggerModel.moveFroggerBy(0, -1);
    } else if (code == KeyCode.RIGHT || code == KeyCode.D) {
      this.froggerModel.moveFroggerBy(0, 1);
    } else if (code == KeyCode.UP || code == KeyCode.W) {
      this.froggerModel.moveFroggerBy(-1, 0);
    } else if (code == KeyCode.DOWN || code == KeyCode.S) {
      this.froggerModel.moveFroggerBy(1, 0);
    } else if (code == KeyCode.N) {
      if(this.froggerModel.isGameWon() || this.froggerModel.isGameLost()){
        this.messageLabel.setText("Get to all four lilypads without dying!");
        this.froggerModel.startNewGame();
      }
    } else if (code == KeyCode.J) {
      System.exit(0);
    } else if (code == KeyCode.P) {
      if(!this.froggerModel.isGameWon() && !this.froggerModel.isGameLost()) {
        this.onPause();
      }
    } else {
      keyRecognized = false;
    }

    if (keyRecognized) {
      //this.froggerView.update(this.froggerModel);
      keyEvent.consume();
    }
  }

  /**
   * Allows for pausing and is used to update the cars and logs.
   */
  private void startTimer() {
    this.timer = new java.util.Timer();
    TimerTask timerTask = new TimerTask() {
      public void run() {
        Platform.runLater(new Runnable() {
          public void run() {
            update();

          }
        });
      }
    };

    long frameTimeInMilliSeconds = (long) (1000.0 / FRAMES_PER_SECOND);
    this.timer.schedule(timerTask, 0, frameTimeInMilliSeconds);
  }

  /**
   * Pauses the game based on keyboard input from the controller.
   */
  public void onPause() {
    if (this.paused) {
      this.startTimer();
    } else {
      this.timer.cancel();
    }
    this.paused = !this.paused;
  }


}
