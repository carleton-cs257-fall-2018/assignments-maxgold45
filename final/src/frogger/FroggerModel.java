/**
 * Max Goldberg and Alexis Engel. This controls the game. It allows the objects to move and controls
 * other back-end features.
 */

package frogger;

import javafx.application.Platform;
import java.util.Timer;
import java.util.TimerTask;
import javafx.fxml.FXML;

public class FroggerModel {

  public enum CellValue {
    GROUND, ROAD, FROG, CAR, LOG, WATER, LILYPAD, COMPLETE
  }

  ;
  final private double FRAMES_PER_SECOND = 100.0;

  private boolean gameOver;
  private Timer timer;
  private boolean paused;

  private CellValue[][] cells;
  private int froggerRow;
  private int froggerColumn;
  private CellValue prevValue;
  private int lilypads;

  private Car car1;


  public FroggerModel(int rowCount, int columnCount) {
    assert rowCount > 0 && columnCount > 0;
    this.cells = new CellValue[rowCount][columnCount];
    this.startNewGame();
  }

  public void startNewGame() {
    this.cells = new CellValue[this.cells.length][this.cells[0].length];
    this.lilypads = 4;
    this.prevValue = CellValue.GROUND; // Frogger starts on ground.
    this.paused = false;
    this.gameOver = false;
    this.initializeGame();
  }

  public boolean isGameLost() {
    return this.gameOver;
  }

  public boolean isGameWon() {
    if (lilypads == 0) {
      return true;
    }
    return false;
  }

  public void spawnFrog() {
    int rowCount = this.cells.length;
    int columnCount = this.cells[0].length;
    this.froggerRow = rowCount - 1;
    this.froggerColumn = columnCount / 2;
    this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;
  }

  /**
   * Sets up the game.
   *
   * TODO: Set backgrounds for everything other than ground.
   */
  private void initializeGame() {
    this.startTimer();
    int rowCount = this.cells.length;
    int columnCount = this.cells[0].length;

    // Set all cells to background values.
    for (int row = 0; row < rowCount; row++) {
      for (int column = 0; column < columnCount; column++) {
        if (row > rowCount / 2 && row < rowCount - 1) {
          this.cells[row][column] = CellValue.ROAD;
        } else if (row < rowCount / 2) {
          this.cells[row][column] = CellValue.WATER;
          if (row == 0 && column % 3 == 1) {
            this.cells[row][column] = CellValue.LILYPAD;
          }
        } else {
          this.cells[row][column] = CellValue.GROUND;
        }
      }
    }
    spawnFrog();
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
            updateAnimation();
          }
        });
      }
    };

    long frameTimeInMilliSeconds = (long) (1000.0 / FRAMES_PER_SECOND);
    this.timer.schedule(timerTask, 0, frameTimeInMilliSeconds);
  }

  /**
   * Move the logs and cars.
   *
   * TODO: We will have a list of logs and a list of cars. This will call their update methods, and
   * if one goes off the screen, it will appear on the other side.
   */
  private void updateAnimation() {
    /**double carTop = this.car1.getY() + this.car1.getLayoutY();
    double carLeft = this.car1.getX() + this.car1.getLayoutX();
    double carRight = carLeft + this.car1.getWidth();

    //leave one side and appear at the other (for cars and logs)
    double carVelocity = this.car1.getVelocity();
    //if(carRight >= this.froggerView)

    this.car1.step();*/
  }

  public int getRowCount() {
    return this.cells.length;
  }

  public int getColumnCount() {
    assert this.cells.length > 0;
    return this.cells[0].length;
  }


  public CellValue getCellValue(int row, int column) {
    assert row >= 0 && row < this.cells.length && column >= 0 && column < this.cells[0].length;
    return this.cells[row][column];
  }

  /**
   * Moves the frog based on keyboard input from the Controller. Doesn't allow the frog to move into
   * the walls.
   *
   * TODO: Kill the frog when it hits a car1 or water.
   */
  public void moveFroggerBy(int rowChange, int columnChange) {
    if (isGameWon()){
      this.froggerRow = froggerColumn = 0;
    }
    else if(isGameLost()){
      this.froggerRow = froggerColumn = 0;
    }
    else if (this.paused) {
      return;
    }
    else {

      int newRow = this.froggerRow + rowChange;
      if (newRow < 0) {
        newRow = 0;
      }
      if (newRow >= this.getRowCount()) {
        newRow = this.getRowCount() - 1;
      }

      int newColumn = this.froggerColumn + columnChange;
      if (newColumn < 0) {
        newColumn = 0;
      }
      if (newColumn >= this.getColumnCount()) {
        newColumn = this.getColumnCount() - 1;
      }

      this.cells[this.froggerRow][this.froggerColumn] = prevValue;

      this.froggerRow = newRow;
      this.froggerColumn = newColumn;
      this.prevValue = this.cells[this.froggerRow][this.froggerColumn];

      if (this.prevValue == CellValue.LILYPAD) {
        this.cells[froggerRow][froggerColumn] = CellValue.COMPLETE;
        this.prevValue = CellValue.GROUND; // Reset the prevValue
        this.lilypads--;
        if (lilypads > 0) {
          spawnFrog();
        }
      }
      else if (this.prevValue == CellValue.WATER){
          //this.gameOver = true;
      }

      this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;

    }
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
