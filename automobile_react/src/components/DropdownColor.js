import React, { Component } from "react";
import {SelectField, MenuItem } from "material-ui";

import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { selectColor } from "../actions";

import { graphql } from "react-apollo";
import AllColors from "../queries/AllColors";

class DropdownColor extends Component{
  constructor(props) {
    super(props);
    this.state = {value: "All"};
  }

  handleColorChange(event, index, value){
    this.setState({value: value});
  }

  renderColorItems(){
    return this.props.data.allColors.map(
      (color) => {
        return(
          <MenuItem
            value={color.id}
            key={color.id}
            primaryText={color.name}
            onTouchTap={() => this.props.selectColor(color.id)}
            >
          </MenuItem>
        );
      }
      
    )
  }

  render(){
    if(this.props.data.loading){
      return <div></div>
    }
    return(
      <SelectField
        value={this.state.value}
        onChange={this.handleColorChange.bind(this)}
        fullWidth={true}
        floatingLabelText={"Select a Color"}>
        <MenuItem
          value={"All"}
          primaryText="All"
          onTouchTap={() => this.props.selectColor("All")}/>
        {this.renderColorItems()}
      </SelectField>
    );
  }
}

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({ selectColor }, dispatch);
}

export default connect(null, mapDispatchToProps)
(graphql(AllColors)(DropdownColor));
