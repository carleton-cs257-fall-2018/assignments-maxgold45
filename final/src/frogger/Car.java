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
      this.img = new ImagePattern(new Image("res/car1Front.png"));
    } else if (imageNum == 1){
      this.img = new ImagePattern(new Image("res/car1Back.png"));
    } else if (imageNum == 2){
      this.img = new ImagePattern(new Image("res/car2Front.png"));
    }else if (imageNum == 3){
      this.img = new ImagePattern(new Image("res/car2Back.png"));
    } else if (imageNum == 4){
      this.img = new ImagePattern(new Image("res/car3Front.png"));
    }else if (imageNum == 5){
      this.img = new ImagePattern(new Image("res/car2Back.png"));
    }
  }
}