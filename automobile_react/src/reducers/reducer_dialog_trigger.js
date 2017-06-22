import { DIALOG_TRIGGERED } from "../actions";

export default (state = false, action) => {
  switch(action.type){
    case DIALOG_TRIGGERED:
      return action.payload;
  }
  return state;
}
