import { useState } from "react";

const PythonRunner = () => {
  const [output, setOutput] = useState("Waiting...");
  const [userInput, setUserInput] = useState("");
  const [loading, setLoading] = useState(false);

  const runHiddenCode = async () => {
    setLoading(true);
    setOutput("Running...");

    try {
      const res = await fetch("http://localhost:5000/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: userInput }),
      });

      const data = await res.json();
      setOutput(data.output);
    } catch (err: any) {
      setOutput("Error: " + err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "monospace" }}>
      <textarea
        placeholder="Type input here..."
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        style={{ width: "100%", height: "100px", marginBottom: "10px" }}
      />
      <button onClick={runHiddenCode} style={{ padding: "10px 20px" }} disabled={loading}>
        {loading ? "Running..." : "Run Hidden Code"}
      </button>
      <h3>Output:</h3>
      <pre style={{ backgroundColor: "#f0f0f0", padding: "15px", border: "1px solid #ccc" }}>
        {output}
      </pre>
    </div>
  );
};

export default PythonRunner;