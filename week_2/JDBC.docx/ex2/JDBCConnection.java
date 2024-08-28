import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCConnection {

    static final String JDBC_URL = "jdbc:mysql://localhost:3306/employee_db";
    static final String USERNAME = "Student";
    static final String PASSWORD = "Student"; 

    public static Connection getConnection() {
        Connection connection = null;
        try {
            
            Class.forName("com.mysql.cj.jdbc.Driver");

            connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
            System.out.println("Connected to the database successfully.");

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
        return connection;
    }

    public static void main(String[] args) {
        
        Connection connection = JDBCConnection.getConnection();
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
                System.out.println("Connection closed.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
