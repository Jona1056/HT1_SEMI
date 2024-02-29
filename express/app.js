const express = require("express")
const app = express();
app.get("/", (req, res) => {
    const data = {
        "Instancia": "Instancia #2 - API #2",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Jonatan Garcia - 202000424"
    };
    res.json(data);
  });

app.get("/check", (req, res) => {
    res.status(200).send("OK");
});

  
app.listen(8081, () => {
    console.log("Server is running on port 8081");
    }   );