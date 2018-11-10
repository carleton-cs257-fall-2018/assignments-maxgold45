/**
 * Max Goldberg and Alexis Engel.
 * This controls the game. It allows the objects to move and controls other back-end features.
 */

package frogger;

import javafx.application.Platform;
import java.util.Timer;
import java.util.TimerTask;


public class FroggerModel {
  public enum CellValue {
    GROUND, FROG, CAR, LOG, TURTLE, WATER, ENDPOINT
  };
  final private double FRAMES_PER_SECOND = 20.0;

  private boolean gameOver;
  private int score;
  private int level;
  private Timer timer;
  private boolean paused;

  private CellValue[][] cells;
  private int froggerRow;
  private int froggerColumn;

  public FroggerModel(int rowCount, int columnCount) {
    assert rowCount > 0 && columnCount > 0;
    this.cells = new CellValue[rowCount][columnCount];
    this.startNewGame();
  }

  public void startNewGame() {
    this.paused = false;
    this.gameOver = false;
    this.score = 0;
    this.level = 1;
    this.initializeGame();
  }

  public boolean isGameOver() {
    return this.gameOver;
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

    // Set all cells to ground.
    for (int row = 0; row < rowCount; row++) {
      for (int column = 0; column < columnCount; column++) {
        this.cells[row][column] = CellValue.GROUND;
      }
    }

    // Place the frog
    this.froggerRow = rowCount - 1;
    this.froggerColumn = columnCount / 2;
    this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;
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

    long frameTimeInMilliSeconds = (long)(1000.0 / FRAMES_PER_SECOND);
    this.timer.schedule(timerTask, 0, frameTimeInMilliSeconds);
  }

  /**
   * Move the logs and cars.
   *
   * TODO:
   * We will have a list of logs and a list of cars. This will call their update methods, and if one
   * goes off the screen, it will appear on the other side.
   */
  private void updateAnimation() {
  }

  public int getRowCount() {
    return this.cells.length;
  }

  public int getColumnCount() {
    assert this.cells.length > 0;
    return this.cells[0].length;
  }

  public int getScore() {
    return this.score;
  }

  public CellValue getCellValue(int row, int column) {
    assert row >= 0 && row < this.cells.length && column >= 0 && column < this.cells[0].length;
    return this.cells[row][column];
  }

  /**
   * Moves the frog based on keyboard input from the Controller. Doesn't allow the frog to move
   * into the walls.
   *
   * TODO: Kill the frog when it hits a car or water.
   */
  public void moveFroggerBy(int rowChange, int columnChange) {
    if (this.gameOver || this.paused) {
      return;
    }

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

    this.cells[this.froggerRow][this.froggerColumn] = CellValue.GROUND;

    this.froggerRow = newRow;
    this.froggerColumn = newColumn;
    this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;

  }

  /**
   * Pauses the game based on keyboard input from the controller.
   */
  public void onPause(){
    if (this.paused) {
      this.startTimer();
    } else {
      this.timer.cancel();
    }
    this.paused = !this.paused;
  }

}
