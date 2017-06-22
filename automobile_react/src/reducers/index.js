import { combineReducers } from 'redux';
import selectedColorReducer from "./reducer_selected_color";
import selectedCarReducer from "./reducer_selected_car"
import dialogTriggerReducer from "./reducer_dialog_trigger";

const rootReducer = combineReducers({
  selected_color: selectedColorReducer,
  selected_car: selectedCarReducer,
  car_dialog_open: dialogTriggerReducer
});

export default rootReducer;
