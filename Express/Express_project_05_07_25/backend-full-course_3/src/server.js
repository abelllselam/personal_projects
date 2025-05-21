import express from "express";
import path, { dirname } from "path";
import { fileURLToPath } from "url";

const app = express();

const PORT = process.env.PORT || 5003;

//get the file path from the URL of the current module
const __filename = fileURLToPath(import.meta.url);

//get the directory name from the file path
const __dirname = dirname(__filename);

//telling it where the public directory is:
//serve all files from the public dir as static assets.

app.use(express.static(path.join(__dirname, "../public")));
app.use(express.json());

//serving up the HTMl file from the /public directory
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../public/index.html"));
});

app.listen(PORT, () => {
  console.log(`Server has started on port: ${PORT}`);
});
