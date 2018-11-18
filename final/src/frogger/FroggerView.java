/**
 * Max Goldberg and Alexis Engel.
 * This will allow the user to see the game.
 */

package frogger;

import frogger.FroggerModel.CellValue;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.paint.Color;
import javafx.scene.paint.ImagePattern;
import javafx.scene.shape.Rectangle;

public class FroggerView extends Group {
  public final static double CELL_WIDTH = 40.0;
  @FXML private int rowCount;
  @FXML private int columnCount;
  private Rectangle[][] cellViews;

  private ImagePattern froggerIMG;
  private ImagePattern roadIMG;
  private ImagePattern waterIMG;
  private ImagePattern lilypadIMG;
  private ImagePattern car1IMG;
  private ImagePattern car2IMG;
  private ImagePattern car3IMG;
  private ImagePattern logIMG;

  public FroggerView() {
    this.waterIMG = new ImagePattern(new Image("res/water.png"));
    this.froggerIMG = new ImagePattern(new Image("/res/frogger.png"));
    this.roadIMG = new ImagePattern(new Image("res/road.png"));
    this.lilypadIMG = new ImagePattern(new Image("res/lilypad.png"));

    this.logIMG = new ImagePattern(new Image("res/log.png"));
  }

  public int getRowCount() {
    return this.rowCount;
  }

  public void setRowCount(int rowCount) {
    this.rowCount = rowCount;
    this.initializeGrid();
  }

  public int getColumnCount() {
    return this.columnCount;
  }

  public void setColumnCount(int columnCount) {
    this.columnCount = columnCount;
    this.initializeGrid();
  }

  /**
   * Sets the background of the game.
   *
   * TODO: Change the background to have water, ground, and road.
   */
  private void initializeGrid() {
    if (this.rowCount > 0 && this.columnCount > 0) {
      this.cellViews = new Rectangle[this.rowCount][this.columnCount];
      for (int row = 0; row < this.rowCount; row++) {
        for (int column = 0; column < this.columnCount; column++) {
          Rectangle rectangle = new Rectangle();
          rectangle.setX((double)column * CELL_WIDTH);
          rectangle.setY((double)row * CELL_WIDTH);
          rectangle.setWidth(CELL_WIDTH);
          rectangle.setHeight(CELL_WIDTH);
          this.cellViews[row][column] = rectangle;
          this.getChildren().add(rectangle);
        }
      }
    }
  }

  /**
   * Moves the frog on the game board given the key inputs from the Controller.
   *
   * TODO: Make it so that the frog will die.
   * TODO: Move logs and cars.
   */
  public void update(FroggerModel model) {
    ImageView im = new ImageView();

    assert model.getRowCount() == this.rowCount && model.getColumnCount() == this.columnCount;
    for (int row = 0; row < this.rowCount; row++) {
      for (int column = 0; column < this.columnCount; column++) {
        FroggerModel.CellValue cellValue = model.getCellValue(row, column);
        if (cellValue == CellValue.FROG || cellValue == CellValue.COMPLETE) {
          this.cellViews[row][column].setFill(this.froggerIMG);
        }
        else if(cellValue == CellValue.CAR) {
          int car = (int)(3*Math.random());

          if(car==0){
            this.cellViews[row][column].setFill(this.car1IMG);
          }
          else if(car==1) {
            this.cellViews[row][column].setFill(this.car2IMG);
          }
          else if(car==2) {
            this.cellViews[row][column].setFill(this.car3IMG);
          }
        }
        else if (cellValue == CellValue.LOG) {
          this.cellViews[row][column].setFill(this.logIMG);
        }
        else if (cellValue == CellValue.ROAD){
          this.cellViews[row][column].setFill(this.roadIMG);
        }
        else if (cellValue == CellValue.WATER) {
          this.cellViews[row][column].setFill(this.waterIMG);
        }
        else if(cellValue == CellValue.LILYPAD){
          this.cellViews[row][column].setFill(lilypadIMG);
        }
        else if (cellValue == CellValue.GROUND){
          this.cellViews[row][column].setFill(Color.GREEN);
        }
        else {
          this.cellViews[row][column].setFill(Color.RED);
        }
      }
    }
  }
}