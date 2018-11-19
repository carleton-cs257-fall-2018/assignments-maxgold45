package frogger;

import frogger.FroggerModel.CellValue;

public class MovingObject {
  protected int velocity; // Positive is right, negative is left.
  protected int row;
  protected int column;
  protected CellValue imageValue;

  public static final int MAX_COLUMN = 12;

  public MovingObject(int velocity, int row, int column) {
    this.velocity = velocity;
    this.row = row;
    this.column = column;
  }

  public int getVelocity(){
    return this.velocity;
  }

  public int getRow() {
    return this.row;
  }

  public int getColumn() {
    return this.column;
  }

  public boolean contains(int row, int column) {
    if (this.row == row && this.column == column) {
      return true;
    }
    return false;
  }

  public void step(){
    this.column = this.column + this.velocity;
    if (this.column >= this.MAX_COLUMN && this.velocity > 0){
      this.column -= this.MAX_COLUMN;
    }
    else if (this.column <= 0 && this.velocity < 0){
      this.column += this.MAX_COLUMN;
    }
  }
  
  public CellValue getImageValue() {
    return imageValue;
  }

}
