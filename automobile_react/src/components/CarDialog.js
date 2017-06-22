import React, { Component } from "react";
import { Dialog, RaisedButton, FlatButton, TextField } from 'material-ui';

import { connect } from "react-redux";
import { bindActionCreators } from "redux";
import { dialogTrigger } from "../actions";

import { graphql } from "react-apollo";
import MoveCarSlotExplicit from "../mutations/MoveCarExplicit";
import query from "../queries/CarByColor"

class CarDialog extends Component{
  constructor(props){
    super(props);
    this.state = {
      open: props.car_dialog_open,
      input: 0,
      errors: ""
    }
  }

  componentWillUpdate(nextProps){
    if(this.props.car_dialog_open != nextProps.car_dialog_open){
      this.setState({open: nextProps.car_dialog_open});
    }
  }

  handleDialog(open){
    this.props.dialogTrigger(open);
    if(!open){
      this.setState({input: 0, errors: ""})
    }
  };

  handleSubmit(event){
    event.preventDefault();
    const { input } = this.state;
    const { selected_car, selected_color } = this.props;
    if(input != "" && input != 0 && input > 0){
      this.props.mutate({
        variables: { id: selected_car.id, slotNumber: input },
        refetchQueries: [{ query, variables: {colorId: selected_color} }]
      }).then(
        ({ data })=> {
          if(data.moveCarSlotExplicit.validationError){
            this.setState({
              errors: data.moveCarSlotExplicit.validationError
            });
          } else {
            this.handleDialog(false);
          }
        }
      )
    } else{
      this.setState({errors: "Please select a slot that is greater than zero."})
    }
  }

  render(){
    const { selected_car } = this.props;
    if(!selected_car){
      return <div></div>
    }
    return(
      <div>
        <Dialog
          title={`Exchange ${selected_car.name} Slot Location`}
          modal={false}
          open={this.state.open}
          onRequestClose={this.handleDialog.bind(this, false)}
          >
          <p>Slot Number: {selected_car.slotNumber}</p>
          <form onSubmit={this.handleSubmit.bind(this)}>
            <TextField
              floatingLabelText="Slot Location"
              hintText="Desired Slot Location"
              fullWidth={true}
              type={'number'}
              value={this.state.input}
              onChange={({target}) => this.setState({input: target.value})}
            />
            <div className="red-text">
              {this.state.errors}
            </div>
            <FlatButton
              label="Submit"
              primary={true}
              type="submit"
            />
            <FlatButton
              label="Cancel"
              primary={true}
              onTouchTap={this.handleDialog.bind(this, false)}
            />
          </form>
        </Dialog>
      </div>
    )
  }
}

const mapStateToProps = ({ selected_color, selected_car, car_dialog_open }) =>{
  return { selected_color, selected_car, car_dialog_open };
}

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({ dialogTrigger }, dispatch);
}
export default connect(mapStateToProps, mapDispatchToProps)(
  graphql(MoveCarSlotExplicit)(CarDialog)
);
