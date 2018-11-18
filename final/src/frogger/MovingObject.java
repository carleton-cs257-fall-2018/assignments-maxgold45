package frogger;

import javafx.scene.paint.ImagePattern;


public class MovingObject {
  protected int velocity; // Positive is right, negative is left.
  protected int row;
  protected int column;
  protected ImagePattern img;

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
  }



}
