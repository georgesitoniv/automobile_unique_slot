import { COLOR_SELECTED } from "../actions";

export default (state = null, action) => {
  switch(action.type){
    case COLOR_SELECTED:
      return action.payload;
  }
  return state;
}
