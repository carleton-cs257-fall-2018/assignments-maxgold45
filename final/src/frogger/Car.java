/**
 * Max Goldberg and Alexis Engel.
 */

package frogger;


import javafx.scene.image.Image;
import javafx.scene.paint.ImagePattern;

public class Car extends MovingObject{

  Car(int velocity, int row, int column, int imageNum){
    super(velocity, row, column);
    if (imageNum == 0){
      this.img = new ImagePattern(new Image("res/car1.png"));

    } else if (imageNum == 1){
      this.img = new ImagePattern(new Image("res/car2.png"));

    } else if (imageNum == 2){
      this.img = new ImagePattern(new Image("res/car3.png"));

    }

//    this.img =
  }
}