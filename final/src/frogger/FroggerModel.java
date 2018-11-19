/**
 * Max Goldberg and Alexis Engel. This controls the game. It allows the objects to move and controls
 * other back-end features.
 */

package frogger;

import javafx.application.Platform;
import java.util.Timer;
import java.util.TimerTask;
import java.util.ArrayList;

public class FroggerModel {

  public enum CellValue {
    GROUND, ROAD, FROG, LOG, WATER, LILYPAD, COMPLETE, CAR1FRONT, CAR1BACK, CAR2FRONT, CAR2BACK,
    CAR3FRONT, CAR3BACK
  }


  private final double FRAMES_PER_SECOND = 1;
  private static final int MAX_VELOCITY = 3;

  private boolean gameOver;
  private Timer timer;
  private boolean paused;

  private CellValue[][] cells;
  private int froggerRow;
  private int froggerColumn;
  private CellValue prevValue;
  private int lilypads;

  private ArrayList<Car> carList;


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
    setUpCars();
    spawnFrog();
  }

  private void setUpCars(){
    carList = new ArrayList<>();

    makeCarPair(11);
    makeCarPair(10);
    makeCarPair(9);
    makeCarPair(8);
    makeCarPair(7);

  }

  private void makeCarPair(int row){
    Car carFront, carBack;
    int velocity = (int)(Math.random() * MAX_VELOCITY + 1);
    int column = (int)(Math.random() * 9) + 1;
    int imageNum = (int)(Math.random() * (3)) * 2; // 0, 2, or 4
    if (imageNum == 4){
      /*carFront = new Car(velocity * -1, row, column, imageNum);
      carBack = new Car(velocity * -1, row, column - 1, imageNum + 1);*/
      imageNum = 2;
      carFront = new Car(velocity, row, column, imageNum);
      carBack = new Car(velocity, row, column - 1, imageNum + 1);
    }
    else {
      carFront = new Car(velocity, row, column, imageNum);
      carBack = new Car(velocity, row, column - 1, imageNum + 1);
    }
    carList.add(carFront);
    carList.add(carBack);
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
    for (int i = 0; i < carList.size(); i += 2) {
      Car carFront = carList.get(i);
      Car carBack = carList.get(i + 1);

      int prevFrontCol = carFront.getColumn();
      int prevBackCol = carBack.getColumn();

      carFront.step();
      carBack.step();

      this.cells[carFront.getRow()][carFront.getColumn()] = carFront.getImageValue();
      this.cells[carBack.getRow()][carBack.getColumn()] = carBack.getImageValue();

      this.cells[carBack.getRow()][prevBackCol] = CellValue.ROAD;
      if (carBack.getVelocity() > 1) {
        this.cells[carFront.getRow()][prevFrontCol] = CellValue.ROAD;
      }
    }
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
    if (isGameWon() || isGameLost()){
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
      else if (this.prevValue == CellValue.CAR1BACK || this.prevValue == CellValue.CAR1FRONT ||
               this.prevValue == CellValue.CAR2BACK || this.prevValue == CellValue.CAR2FRONT ||
               this.prevValue == CellValue.CAR3BACK || this.prevValue == CellValue.CAR3FRONT ||
               this.prevValue == CellValue.WATER){
        this.gameOver = true;
        this.onPause();
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
