import { useState } from "react";
import "./App.css";

export default function App() {
  const [display, setDisplay] = useState("");

  function addChar(char: string) {
    setDisplay(display + char);
  }

  function clearDisplay() {
    setDisplay("");
  }

  function calculate() {
    try {
      // eval usado apenas para fins didáticos
      const result = eval(display);
      setDisplay(String(result));
    } catch {
      setDisplay("Erro");
    }
  }

  return (
    <div className="calc">
      <input type="text" value={display} readOnly />

      <div className="keys">
        <button onClick={() => addChar("7")}>7</button>
        <button onClick={() => addChar("8")}>8</button>
        <button onClick={() => addChar("9")}>9</button>
        <button onClick={() => addChar("/")}>/</button>

        <button onClick={() => addChar("4")}>4</button>
        <button onClick={() => addChar("5")}>5</button>
        <button onClick={() => addChar("6")}>6</button>
        <button onClick={() => addChar("*")}>*</button>

        <button onClick={() => addChar("1")}>1</button>
        <button onClick={() => addChar("2")}>2</button>
        <button onClick={() => addChar("3")}>3</button>
        <button onClick={() => addChar("-")}>-</button>

        <button onClick={() => addChar("0")}>0</button>
        <button onClick={() => addChar(".")}>.</button>
        <button onClick={calculate}>=</button>
        <button onClick={() => addChar("+")}>+</button>
      </div>

      <button className="wide" onClick={clearDisplay}>Limpar</button>
    </div>
  );
}
