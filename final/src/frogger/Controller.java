/**
 * Max Goldberg and Alexis Engel.
 * This will allow the user to control the frog.
 */

package frogger;

import javafx.fxml.FXML;
import javafx.event.EventHandler;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class Controller implements EventHandler<KeyEvent> {
  @FXML private Label messageLabel;
  @FXML private FroggerView froggerView;
  private FroggerModel froggerModel;

  public Controller() {
  }

  public void initialize() {
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
  private void update() {
    this.froggerView.update(this.froggerModel);
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
        this.froggerModel.onPause();
      }
    } else {
      keyRecognized = false;
    }

    if (keyRecognized) {
      this.update();
      keyEvent.consume();
    }
  }

}
