/**
 * Max Goldberg and Alexis Engel.
 * Create the Frogger window.
 */

package frogger;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {
    public void start(Stage primaryStage) throws Exception{
        FXMLLoader loader = new FXMLLoader(getClass().getResource("frogger.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("Frogger");

        Controller controller = loader.getController();
        root.setOnKeyPressed(controller);
        double sceneWidth = controller.getBoardWidth();
        double sceneHeight = controller.getBoardHeight();
        primaryStage.setScene(new Scene(root, sceneWidth, sceneHeight));
        primaryStage.setMaximized(true);
        primaryStage.show();
        root.requestFocus();
    }


    public static void main(String[] args) {
        launch(args);
    }
}
