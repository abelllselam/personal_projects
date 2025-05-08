const express = require("express");
const app = express();
const PORT = 8383;

//middleware
app.use(express.json());

//data
let data = ["james"];

app.get("/", (req, res) => {
  res.send(`<body style="background: pink; color:blue;">
    <h1>Data:</h1>
      <p>${JSON.stringify(data)}</p>
      <a href="/dashboard">Dashboard</a>
    </body>`);
});

app.get("/dashboard", (req, res) => {
  console.log("ohhh now i hit the /dashboard endpoint");
  res.send(`<body>
      <h1>Dashboard</h1>
      <a href="/">Home</a>
    </body>`);
});

app.get("/api/data", (req, res) => {
  console.log("This one was for data");
  res.status(599).send(data);
});

app.post("/api/data", (req, res) => {
  //They want to create a button when they want to signup botton
  const newEntry = req.body;
  console.log(newEntry);
  data.push(newEntry.name);
  res.sendStatus(201);
});

app.delete("/api/data", (req, res) => {
  data.pop();
  console.log("We delete the index value of the end of the array");
  res.sendStatus(203);
});

app.listen(PORT, () => {
  console.log(`Server has started on ${PORT}`);
});
