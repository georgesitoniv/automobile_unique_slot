import { CAR_SELECTED } from "../actions";

export default (state = null, action) => {
  switch(action.type){
    case CAR_SELECTED:
      return action.payload;
  }
  return state;
}
