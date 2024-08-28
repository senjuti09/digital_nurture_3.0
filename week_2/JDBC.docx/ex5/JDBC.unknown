import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;
import java.util.Scanner;

public class EmployeeManagementApp {

    static final String JDBC_URL = "jdbc:mysql://localhost:3306/employee_db";
    static final String USERNAME = "Student";
    static final String PASSWORD = "Student";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        EmployeeDataRetrieval dataRetrieval = new EmployeeDataRetrieval();

        while (true) {
            System.out.println("Choose an operation:");
            System.out.println("1. Add Employee");
            System.out.println("2. Update Employee");
            System.out.println("3. Delete Employee");
            System.out.println("4. View Employees");
            System.out.println("5. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); 

            switch (choice) {
                case 1:
                    // Add Employee
                    System.out.print("Enter name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter position: ");
                    String position = scanner.nextLine();
                    System.out.print("Enter salary: ");
                    double salary = scanner.nextDouble();
                    scanner.nextLine(); 
                    dataRetrieval.addEmployee(name, position, salary);
                    break;

                case 2:
                    // Update Employee
                    System.out.print("Enter employee ID to update: ");
                    int updateId = scanner.nextInt();
                    scanner.nextLine(); 
                    System.out.print("Enter new name: ");
                    String updateName = scanner.nextLine();
                    System.out.print("Enter new position: ");
                    String updatePosition = scanner.nextLine();
                    System.out.print("Enter new salary: ");
                    double updateSalary = scanner.nextDouble();
                    scanner.nextLine(); 
                    dataRetrieval.updateEmployee(updateId, updateName, updatePosition, updateSalary);
                    break;

                case 3:
                    // Delete Employee
                    System.out.print("Enter employee ID to delete: ");
                    int deleteId = scanner.nextInt();
                    scanner.nextLine(); 
                    dataRetrieval.deleteEmployee(deleteId);
                    break;

                case 4:
                    // View Employees
                    System.out.println("Employees:");
                    dataRetrieval.getEmployees();
                    break;

                case 5:
                    // Exit
                    System.out.println("Exiting...");
                    scanner.close();
                    System.exit(0);
                    break;

                default:
                    System.out.println("Invalid choice. Please enter a number between 1 and 5.");
            }
        }
    }

    static class EmployeeDataRetrieval {

        public void addEmployee(String name, String position, double salary) {
            Connection connection = null;
            PreparedStatement preparedStatement = null;

            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

                String sql = "INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)";
                preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setString(1, name);
                preparedStatement.setString(2, position);
                preparedStatement.setDouble(3, salary);

                int rowsAffected = preparedStatement.executeUpdate();
                if (rowsAffected > 0) {
                    System.out.println("Employee added successfully.");
                }

            } catch (ClassNotFoundException | SQLException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (preparedStatement != null) preparedStatement.close();
                    if (connection != null) connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

        public void updateEmployee(int id, String name, String position, double salary) {
            Connection connection = null;
            PreparedStatement preparedStatement = null;

            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

                String sql = "UPDATE employees SET name=?, position=?, salary=? WHERE id=?";
                preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setString(1, name);
                preparedStatement.setString(2, position);
                preparedStatement.setDouble(3, salary);
                preparedStatement.setInt(4, id);

                int rowsAffected = preparedStatement.executeUpdate();
                if (rowsAffected > 0) {
                    System.out.println("Employee updated successfully.");
                } else {
                    System.out.println("Employee not found.");
                }

            } catch (ClassNotFoundException | SQLException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (preparedStatement != null) preparedStatement.close();
                    if (connection != null) connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

        public void deleteEmployee(int id) {
            Connection connection = null;
            PreparedStatement preparedStatement = null;

            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                connection = DriverManager.getConnection(JDBC_URL, USERNAME, PASSWORD);

                String sql = "DELETE FROM employees WHERE id=?";
                preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setInt(1, id);

                int rowsAffected = preparedStatement.executeUpdate();
                if (rowsAffected > 0) {
                    System.out.println("Employee deleted successfully.");
                } else {
                    System.out.println("Employee not found.");
                }

            } catch (ClassNotFoundException | SQLException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (preparedStatement != null) preparedStatement.close();
                    if (connection != null) connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

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
    }
}
