import React, { Component } from "react";
import { DropDownMenu, MenuItem, AppBar } from 'material-ui';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

import DropdownColor from "./DropdownColor";
import CarList from "./CarList";
import CarDialog from "./CarDialog";

class App extends Component{

  render(){
    return(
      <MuiThemeProvider>
        <div>
          <AppBar
            title="Automobile"
          />
          <div className="container">
            <DropdownColor/>
            <CarList/>
            <CarDialog/>
          </div>
        </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
