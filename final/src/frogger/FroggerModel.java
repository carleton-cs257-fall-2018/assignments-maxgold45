/**
 * Max Goldberg and Alexis Engel. This controls the game. It allows the objects to move and controls
 * other back-end features.
 */

package frogger;

import java.util.ArrayList;

public class FroggerModel {

  public enum CellValue {
    GROUND, ROAD, FROG, LOG, WATER, LILYPAD, COMPLETE, CAR1FRONT, CAR1BACK, CAR2FRONT, CAR2BACK,
    CAR3FRONT, CAR3BACK
  }

  private static final int MAX_VELOCITY = 2;
  private static final int MAX_LILYPAD = 4;

  private CellValue[][] cells;
  private boolean gameOver;

  private int froggerRow;
  private int froggerColumn;
  private CellValue prevValue;
  private int lilypads;

  private ArrayList<Car> carList;
  private ArrayList<Log> logList;

  public FroggerModel(int rowCount, int columnCount) {
    assert rowCount > 0 && columnCount > 0;
    this.cells = new CellValue[rowCount][columnCount];
    this.startNewGame();
  }

  public void startNewGame() {
    this.cells = new CellValue[this.cells.length][this.cells[0].length];
    this.lilypads = MAX_LILYPAD;
    this.prevValue = CellValue.GROUND; // Frogger starts on ground.
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

  private void initializeGame() {
    int rowCount = this.cells.length;
    int columnCount = this.cells[0].length;

    // Set all cells to background values.
    for (int row = 0; row < rowCount; row++) {
      for (int column = 0; column < columnCount; column++) {
        if (row > rowCount / 2 && row < rowCount - 1) {
          this.cells[row][column] = CellValue.ROAD;
        }
        else if (row < rowCount / 2) {
          this.cells[row][column] = CellValue.WATER;
          if (row == 0 && column % 3 == 1) {
            this.cells[row][column] = CellValue.LILYPAD;
          }
        }
        else {
          this.cells[row][column] = CellValue.GROUND;
        }
      }
    }
    setUpObjects();
    updateAnimation();
  }

  private void setUpObjects(){
    carList = new ArrayList<>();
    logList = new ArrayList<>();

    // Make one car per row.
    makeCarPair(11);
    makeCarPair(10);
    makeCarPair(9);
    makeCarPair(8);
    makeCarPair(7);

    // Make one log per row.
    makeLogSet(5, -1);
    makeLogSet(4, 1);
    makeLogSet(3, -1);
    makeLogSet(2, 1);
    makeLogSet(1, -1);

    spawnFrog();
  }

  /**
   * Create a car given a row.
   * Each car on the screen will be 2 Log objects next to each other with different images.
   *
   * Work in progress: Making a car move backwards. We aren't currently using the backwards
   * car images.
   */
  private void makeCarPair(int row) {
    Car carFront, carBack;
    int velocity = (int)(Math.random() * MAX_VELOCITY + 1);
    if((int)(Math.random() * 2) == 0){
      velocity *= -1;
    }
    int column = (int) (Math.random() * 9) + 1;
    int imageNum = (int) (Math.random() * (2)) * 2; // 0 or 2
    if (velocity < 0){
      imageNum = 4;
    }

    carFront = new Car(velocity, row, column, imageNum);
    carBack = new Car(velocity, row, column - 1, imageNum + 1);

    if (carFront.getVelocity() > 0) {
      carList.add(carFront);
      carList.add(carBack);
    }
    else{
      carList.add(carBack);
      carList.add(carFront);
    }

  }

  /**
   * Create a log given a row.
   * Each log on the screen will be 3 Log objects next to each other.
   */
  private void makeLogSet(int row, int velocity) {
    Log log1, log2, log3;
    int column = (int)(Math.random() * 8) + 1;

    log1 = new Log(velocity, row, column);
    log2 = new Log(velocity, row, column + 1);
    log3 = new Log(velocity, row, column + 2);

    if (velocity > 0) {
      logList.add(log1);
      logList.add(log2);
      logList.add(log3);
    }
    else{
      logList.add(log3);
      logList.add(log2);
      logList.add(log1);
    }

  }

  private void spawnFrog() {
    int rowCount = this.cells.length;
    int columnCount = this.cells[0].length;
    this.froggerRow = rowCount - 1;
    this.froggerColumn = columnCount / 2;
    this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;
  }
  /**
   * Move the logs and cars.
   */
  public void updateAnimation() {
    updateCars();
    updateLogs();
  }

  /**
   * This will move the cars according to the timer. It will also kill the frog if it's run over.
   */
  private void updateCars() {
    for (int i = 0; i < carList.size(); i += 2) {
      Car carFront = carList.get(i);
      Car carBack = carList.get(i + 1);

      int prevFrontCol = carFront.getColumn();
      int prevBackCol = carBack.getColumn();


      carFront.step();
      carBack.step();

      // If the car ran over the frog, end the game.
      if (carBack.contains(froggerRow, froggerColumn) ||
          carFront.contains(froggerRow, froggerColumn)){// || (carBack.getVelocity() == 2 && carBack.contains(froggerRow, froggerColumn - 1))){
        this.gameOver = true;
      }

      this.cells[carFront.getRow()][carFront.getColumn()] = carFront.getImageValue();
      this.cells[carBack.getRow()][carBack.getColumn()] = carBack.getImageValue();

      this.cells[carBack.getRow()][prevBackCol] = CellValue.ROAD;
      if (carBack.getVelocity() > 1 || carBack.getVelocity() < -1) {
        this.cells[carFront.getRow()][prevFrontCol] = CellValue.ROAD;
      }
    }
  }

  /**
   * This method updates the logs according to the timer, and also moves the frog
   * when it is on a log.
   */
  private void updateLogs() {
    for (int i = 0; i < logList.size(); i += 3) {
      Log logBack = logList.get(i);
      Log logMidd = logList.get(i+1);
      Log logFront = logList.get(i+2);

      int prevBackCol = logBack.getColumn();
      int prevMiddCol = logMidd.getColumn();
      int prevFrontCol = logFront.getColumn();
      boolean hasFrog = false;

      // Show the frog if it's on the log.
      if (logFront.contains(froggerRow, froggerColumn)){
        this.cells[logFront.getRow()][logFront.getColumn()] = CellValue.FROG;
        hasFrog = true;
      }
      else if (logMidd.contains(froggerRow, froggerColumn)){
        this.cells[logMidd.getRow()][logMidd.getColumn()] = CellValue.FROG;
        hasFrog = true;
      }
      else if(logBack.contains(froggerRow,froggerColumn)){
        this.cells[logBack.getRow()][logBack.getColumn()] = CellValue.FROG;
        hasFrog = true;
      }


      logFront.step();
      logMidd.step();
      logBack.step();

      this.cells[logFront.getRow()][logFront.getColumn()] = logFront.getImageValue();
      this.cells[logMidd.getRow()][logMidd.getColumn()] = logMidd.getImageValue();
      this.cells[logBack.getRow()][logBack.getColumn()] = logBack.getImageValue();

      if (hasFrog) {
        moveFroggerBy(0, logMidd.getVelocity());
      }

      this.cells[logBack.getRow()][prevBackCol] = CellValue.WATER;
      if (logBack.getVelocity() > 1) {
        this.cells[logMidd.getRow()][prevMiddCol] = CellValue.WATER;
      }
      if (logBack.getVelocity() > 2) {
        this.cells[logFront.getRow()][prevFrontCol] = CellValue.WATER;
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
   */
  public void moveFroggerBy(int rowChange, int columnChange) {
    if (isGameWon() || isGameLost()){
      this.froggerRow = froggerColumn = 0;
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
        newColumn += MovingObject.MAX_COLUMN;
      }
      if (newColumn >= this.getColumnCount()) {
        newColumn -= MovingObject.MAX_COLUMN;
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
      }

      this.cells[this.froggerRow][this.froggerColumn] = CellValue.FROG;
    }
  }
}