import React, { Component } from "react";
import {
  Card, CardActions,
  CardHeader, CardText,
  FlatButton, RaisedButton, FloatingActionButton, FontIcon
} from 'material-ui';

import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { dialogTrigger, selectCar } from "../actions";

import { graphql } from "react-apollo";
import MoveCar from "../mutations/MoveCar";
import query from "../queries/CarByColor";

class CarDetail extends Component{
  constructor(props){
    super(props)
    this.state = {btnMoveDisabled: false};
  }

  handleDialog(){
    const { dialogTrigger, selectCar, car} = this.props;
    dialogTrigger(true);
    selectCar(car)
  }

  handleMoveCar(direction){
    const { mutate, car, selected_color } = this.props;
    this.setState({btnMoveDisabled: true});
    mutate({
      variables:{ carID: car.id, direction },
      refetchQueries: [{ query, variables: {colorId: selected_color} }]
    }).then(()=> this.setState({btnMoveDisabled: false}));
  }

  render(){
    const { car } = this.props;
    return(
      <div className="col col-md-3 margin-vertical-10" >
        <Card expanded={true} >
          <CardHeader
            title={car.name}
            subtitle={`Slot Number: ${car.slotNumber}`}
            onClick={()=>console.log("click div")}
          />
          <CardText>
            <div className={`circle-block ${car.color.name.toLowerCase()}`}>
            </div>
          </CardText>
          <CardActions>
              <div className="center-block">
              <FloatingActionButton mini={true}
                disabled={this.state.btnMoveDisabled}
                onTouchTap={this.handleMoveCar.bind(this, -1)}
                className="margin-5"
                >
                <FontIcon className="material-icons">keyboard_arrow_up</FontIcon>
              </FloatingActionButton>
              <FloatingActionButton mini={true}
                disabled={this.state.btnMoveDisabled}
                onTouchTap={this.handleMoveCar.bind(this, 1)}
                className="margin-5 btn-move-car"
                >
                <FontIcon className="material-icons">keyboard_arrow_down</FontIcon>
              </FloatingActionButton>
              <FloatingActionButton mini={true}
                disabled={this.state.btnMoveDisabled}
                onTouchTap={this.handleDialog.bind(this)}
                className="margin-5"
                >
                <FontIcon className="material-icons">more_vert</FontIcon>
              </FloatingActionButton>
            </div>
          </CardActions>
        </Card>
      </div>
    )
  }
}

const mapStateToProps = ({selected_color}) => { return { selected_color }; }

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({ dialogTrigger, selectCar }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)
(graphql(MoveCar)(CarDetail));
