import React, {useState} from "react";
import "../css/app.css";
import PageTemplateComponent from "../Components/PageTemplateComponent";
import CalendarComponent from "../Components/CalendarComponent";
import MainEditorComponent from "../Components/MainEditorComponent";
import ListsAndTasksComponent from "../Components/ListsAndTasksComponent";


const MyProfile = () => {

  const [index, setIndex] = useState(0)
  const [list, setList] = useState(null)

  return (
    <div className="mainWrapper">
    <PageTemplateComponent>
      <div className="row" id="box">
        <div id="headerWrapper" className="col-12 ">
        <div className="jumbotron jumbotron-fluid">
          <div className="container">
            <h1 className="display-4">Fluid jumbotron</h1>
            <p className="lead">This is a modified jumbotron that occupies the entire horizontal space of its
              parent.</p>
          </div>
        </div>
        </div>
      </div>
      <div id="mainColumns" className="row d-flex justify-content-between">
        <ListsAndTasksComponent
          onIndexChange={(index1) => setIndex(index1)}
          onListChange={(list1)=> setList(list1)}
        />
        <MainEditorComponent index={index} list={list}/>
        <CalendarComponent/>
      </div>
    </PageTemplateComponent>
    </div>
  )
}

export default MyProfile