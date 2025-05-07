const express = require("express");
const app = express();
const PORT = 8383;

app.get("/", (req, res) => {
  console.log("Yay i hit an endpoint", req.method);
  res.sendStatus(201);
});

app.get("/dashboard", (req, res) => {
  console.log("ohhh now i hit the /dashboard endpoint");
  res.send("Hi");
});

app.listen(PORT, () => {
  console.log(`Server has started on ${PORT}`);
});
