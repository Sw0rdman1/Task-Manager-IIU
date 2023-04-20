import { useEffect, useState } from "react";
import "./App.css";
import TasksSection from "./TasksSection";
import { urlToFlask } from "./utility";

function App() {
  const [tasks, setTasks] = useState([]);

  const fetchFlask = async () => {
    let response = await fetch(urlToFlask("tasks"));
    let json = await response.json();
    return json;
  };

  useEffect(() => {
    fetchFlask().then((res) => {
      setTasks([...res]);
    });
  }, []);

  return (
    <div className="App">
      <nav className="navbar-container">
        <h2>Task Manager</h2>
      </nav>
      <TasksSection tasks={tasks} setTasks={setTasks} />
    </div>
  );
}

export default App;
