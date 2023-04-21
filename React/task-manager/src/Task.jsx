import React, { useEffect, useState } from "react";
import { Checkmark } from "./assets/Checkmark";
import { urlToFlask } from "./utility";
import BinPng from "./assets/bin.png";

const Task = ({ setTasks, task }) => {
  const boolean = task.done ? true : false;
  const [isDone, setIsDone] = useState(boolean);
  console.log(isDone);

  const deleteHandler = async () => {
    const response = await fetch(urlToFlask(`/tasks/${task.id}`), {
      method: "DELETE",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id: task.id }),
    });
    let json = await response.json();
    setTasks([...json]);
  };

  const updateTaskInFlask = async () => {
    await fetch(urlToFlask(`/tasks/${task.id}`), {
      method: "PUT",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ done: !isDone }),
    });
  };

  const clickDoneHandler = () => {
    updateTaskInFlask();
    setIsDone(!isDone);
  };

  return (
    <div className="task-delete-container">
      <div className={isDone ? "task-container-done" : "task-container"}>
        <div>
          <h3>{task.title}</h3>
          <p>{task.description}</p>
        </div>
        <span
          onClick={clickDoneHandler}
          className={isDone ? "checkbox done" : "checkbox "}
        >
          {isDone ? <Checkmark size="26px" /> : <></>}
        </span>
      </div>
      <img
        src={BinPng}
        width={"26px"}
        onClick={deleteHandler}
        className={isDone ? "show-delete" : "hide-delete"}
      />
    </div>
  );
};

export default Task;
