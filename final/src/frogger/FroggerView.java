/**
 * Max Goldberg and Alexis Engel.
 * This will allow the user to see the game.
 */

package frogger;

import frogger.FroggerModel.CellValue;
import javafx.fxml.FXML;
import javafx.scene.Group;
import javafx.scene.image.ImageView;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class FroggerView extends Group {
  public final static double CELL_WIDTH = 20.0;
  @FXML private int rowCount;
  @FXML private int columnCount;
  private Rectangle[][] cellViews;

  public FroggerView() {
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
        if (cellValue == CellValue.FROG) {
          this.cellViews[row][column].setFill(Color.GREEN);
        }  else {
          this.cellViews[row][column].setFill(Color.WHITE);
        }
      }
    }
  }
}