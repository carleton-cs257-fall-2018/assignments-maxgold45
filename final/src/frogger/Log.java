/**
 * Max Goldberg and Alexis Engel.
 */

package frogger;

import frogger.FroggerModel.CellValue;


public class Log extends MovingObject {

    public Log(int velocity, int row, int column) {
      super(velocity, row, column);
      this.imageValue = CellValue.LOG;
    }
}
