const express = require("express");
const mysql = require("mysql2");
const app = express();
const bodyParser = require("body-parser");
const port = 2022;

const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "data",
});

//
app.use(bodyParser.json());

// CREATE(insert)
app.post("/users", (req, res) => {
  const { firstname,lastname,contact,address,email } = req.body;

  connection.query(
    "INSERT INTO users (firstname,lastname,contact,address,email) VALUES (?,?,?,?,?)",
    [firstname,lastname,contact,address,email],
    (err, results) => {
      try {
        if (results.affectedRows > 0) {
          res.json({ message: "Data has been added!" });
        } else {
          res.json({ message: "Something went wrong." });
        }
      } catch (err) {
        res.json({ message: err });
      }
    }
  );
});

// READ (select)
app.get("/users", (req, res) => {
  connection.query("SELECT * FROM users", (err, results) => {
    try {
      if (results.length > 0) {
        res.json(results);
      }
    } catch (err) {
      res.json({ message: err });
    }
  });
});

// UPDATE (update)
app.put("/users", (req, res) => {
  const { lastname, address, id} = req.body;

  if (id && lastname && address) {
    connection.query(
      "UPDATE users SET lastname = ?, address = ? WHERE id = ?",
      [lastname, address, id],
      (err, results) => {
        try {
          if (results.affectedRows > 0) {
            res.json({ message: "Data has been updated!" });
          } else {
            res.json({ message: "Something went wrong." });
          }
        } catch (err) {
          res.json({ message: err });
        }
      }
    );
  } else if (id && lastname) {
    connection.query(
      "UPDATE users SET lastname = ? WHERE id = ?",
      [lastname, id],
      (err, results) => {
        try {
          if (results.affectedRows > 0) {
            res.json({ message: "Data has been updated!" });
          } else {
            res.json({ message: "Something went wrong." });
          }
        } catch (err) {
          res.json({ message: err });
        }
      }
    );
  }
});

// DELETE
app.delete("/users", (req, res) => {
  const { id } = req.body;

  connection.query("DELETE FROM users WHERE id = ?", [id], (err, results) => {
    try {
      if (results.affectedRows > 0) {
        res.json({ message: "Data has been deleted!" });
      } else {
        res.json({ message: "Something went wrong." });
      }
    } catch (err) {
      res.json({ message: err });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});