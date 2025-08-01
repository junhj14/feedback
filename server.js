const express = require("express");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

app.post("/api/feedback", (req, res) => {
  const { message } = req.body;
  if (!message) return res.status(400).send("Message required");
  console.log("Feedback:", message);
  res.json({ success: true });
});

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
