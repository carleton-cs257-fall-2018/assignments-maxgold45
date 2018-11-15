/**
 * Max Goldberg and Alexis Engel.
 */

package frogger;

import javafx.fxml.FXML;
import javafx.scene.shape.Rectangle;

public class Car extends Rectangle{
  @FXML private double velocity; // Positive is right, negative is left.


  public Car() {
  }

  /**
   * Update the car's location.
   */
  public void step() {
    this.setX(this.getX() + this.velocity);

  }

  public double getVelocity(){
    return velocity;
  }

  public void setVelocity(double velocity){
    this.velocity = velocity;
  }
}
