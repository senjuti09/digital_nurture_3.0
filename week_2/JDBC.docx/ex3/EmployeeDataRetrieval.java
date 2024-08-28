import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class EmployeeDataRetrieval {

    static final String JDBC_URL = "jdbc:mysql://localhost:3306/employee_db";
    static final String USERNAME = "Student";
    static final String PASSWORD = "Student";

    public void getEmployees() {
        Connection connection = null;
        Statement statement = null;
        ResultSet resultSet = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);
            statement = connection.createStatement();
            String sql = "SELECT id, name, position, salary FROM employees";
            resultSet = statement.executeQuery(sql);

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                String position = resultSet.getString("position");
                double salary = resultSet.getDouble("salary");

                System.out.printf("ID: %d, Name: %s, Position: %s, Salary: %.2f%n", id, name, position, salary);
            }

        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (resultSet != null) resultSet.close();
                if (statement != null) statement.close();
                if (connection != null) connection.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        EmployeeDataRetrieval dataRetrieval = new EmployeeDataRetrieval();
        dataRetrieval.getEmployees();
    }
}
