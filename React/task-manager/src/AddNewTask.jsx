import React, { useState } from "react";
import { urlToFlask } from "./utility";
import BinPng from "./assets/bin.png";

const AddNewTask = ({ setTasks }) => {
  const [inputOpen, setInputOpen] = useState(false);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const cancelHandler = () => {
    setInputOpen(false);
    setTitle("");
    setDescription("");
  };

  const createTaskObject = () => {
    return {
      title: title,
      content: description,
      done: false,
    };
  };

  const saveHandler = async () => {
    let response = await fetch(urlToFlask("tasks/create"), {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(createTaskObject()),
    });
    let json = await response.json();
    setTasks([...json]);
    setInputOpen(false);
    setTitle("");
    setDescription("");
  };

  return (
    <div className="new-task-container">
      <div className="icon-container">
        <div className={inputOpen ? "add-new-task-input" : "add-new-task"}>
          {!inputOpen ? (
            <span
              className="add-new-task-text"
              onClick={() => setInputOpen(true)}
            >
              +
            </span>
          ) : (
            <>
              <input
                className="title-input"
                placeholder="Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
              <input
                className="description-input"
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </>
          )}
        </div>
        <img src={BinPng} width={"26px"} className={"hide-delete"} />
      </div>
      {inputOpen ? (
        <div className="buttons">
          <button className="save" onClick={saveHandler}>
            Save
          </button>
          <button className="cancel" onClick={cancelHandler}>
            Cancel
          </button>
        </div>
      ) : (
        <></>
      )}
    </div>
  );
};

export default AddNewTask;
