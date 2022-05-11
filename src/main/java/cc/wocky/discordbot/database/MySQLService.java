package cc.wocky.discordbot.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import net.dv8tion.jda.api.entities.Member;

public class MySQLService {

    public void createUser(Member member, String username, String password) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection("url", "Citadel", "password");
            String query = "INSERT INTO users(username, password, user_id) VALUES(?,?,?)";
            PreparedStatement preparedStatement = connection.prepareStatement(query);
            preparedStatement.setString(0, username);
            preparedStatement.setString(1, password);
            preparedStatement.setString(2, member.getUser().getId());
            preparedStatement.execute();
            connection.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteUser(Member member, String username) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection connection = DriverManager.getConnection("url", "Citadel", "password");
            String query = "DELETE FROM users WHERE username=" + username;
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);
            resultSet.close();
            statement.close();
            connection.close();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // public void editUser(Member member, String username) {
    //     try {
    //         Class.forName("com.mysql.cj.jdbc.Driver");
    //         Connection connection = DriverManager.getConnection("url", "Citadel", "password");
    //         String query = "INSERT INTO users(username, password, user_id) VALUES(?,?,?)";
    //         PreparedStatement preparedStatement = connection.prepareStatement(query);
    //         preparedStatement.setString(0, username);
    //         preparedStatement.setString(1, password);
    //         preparedStatement.setString(2, member.getUser().getId());
    //         preparedStatement.execute();
    //         connection.close();
    //     } catch (ClassNotFoundException e) {
    //         e.printStackTrace();
    //     } catch (SQLException e) {
    //         e.printStackTrace();
    //     }
    // }

}
