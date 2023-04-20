import React from "react";
import Task from "./Task";
import AddNewTask from "./AddNewTask";

const TasksSection = ({ tasks, setTasks }) => {
  return (
    <div className="tasks-section-container">
      {tasks.map((task, id) => {
        return <Task key={task.id} task={task} setTasks={setTasks} />;
      })}
      <AddNewTask setTasks={setTasks} />
    </div>
  );
};

export default TasksSection;
