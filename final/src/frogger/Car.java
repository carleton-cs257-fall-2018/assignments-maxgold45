/**
 * Max Goldberg and Alexis Engel.
 */

package frogger;


import frogger.FroggerModel.CellValue;

public class Car extends MovingObject{

  private CellValue oppositeImageValue;

  Car(int velocity, int row, int column, int imageNum){
    super(velocity, row, column);
    switch (imageNum){
      case 0:
        this.imageValue = CellValue.CAR1FRONT;
        this.oppositeImageValue = CellValue.CAR1BACK;
        break;
      case 1:
        this.imageValue = CellValue.CAR1BACK;
        this.oppositeImageValue = CellValue.CAR1FRONT;
        break;
      case 2:
        this.imageValue = CellValue.CAR2FRONT;
        this.oppositeImageValue = CellValue.CAR2BACK;
        break;
      case 3:
        this.imageValue = CellValue.CAR2BACK;
        this.oppositeImageValue = CellValue.CAR2FRONT;
        break;
      case 4:
        this.imageValue = CellValue.CAR3BACK;
        this.oppositeImageValue = CellValue.CAR3FRONT;
        break;
      case 5:
        this.imageValue = CellValue.CAR3FRONT;
        this.oppositeImageValue = CellValue.CAR3BACK;
        break;
    }
  }

}