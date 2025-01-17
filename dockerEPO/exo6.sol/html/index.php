<?php
$conn = new mysqli("db", "user", "password", "myapp");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$result = $conn->query("SELECT * FROM users");
echo "<h1>Users in the database:</h1>";
echo "<ul>";
while($row = $result->fetch_assoc()) {
    echo "<li>" . $row["name"] . "</li>";
}
echo "</ul>";
$conn->close();
?>
