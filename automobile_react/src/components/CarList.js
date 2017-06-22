import React, { Component } from "react";
import {Card, CardActions, CardHeader, CardText, FlatButton} from 'material-ui';

import { connect } from "react-redux";

import { graphql } from "react-apollo";
import query from "../queries/CarByColor";

import CarDetail from "./CarDetail";

class CarList extends Component{

  componentWillUpdate(nextProps){
    if(this.props.selected_color != nextProps.selected_color){
      nextProps.data.refetch({colorId: nextProps.selected_color});
    }
  }

  renderCars(){
    return this.props.data.carByColor.map(
      (car) => {
        return(
          <CarDetail car={car} key={car.id}/>
        );
      }
    );
  }

  render(){
    if(this.props.data.loading){
      return <div>Loading...</div>
    }
    return(
      <div className="row">
        {this.renderCars()}
      </div>
    );
  }
}

const mapStateToProps = ({selected_color}) => { return { selected_color } }

export default connect(mapStateToProps)(
  graphql(query, {
    options: ({selected_color}) => ({ variables: { colorId: selected_color }})
  })
(CarList));
