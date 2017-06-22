
export const COLOR_SELECTED = "COLOR_SELECTED";
export const CAR_SELECTED = "CAR_SELECTED";
export const DIALOG_TRIGGERED = "DIALOG_TRIGGERED";

export function selectColor(color){
  return{
    type: COLOR_SELECTED,
    payload: color
  }
}

export function selectCar(car){
  return{
    type: CAR_SELECTED,
    payload: car
  }
}

export function dialogTrigger(open){
  return{
    type: DIALOG_TRIGGERED,
    payload: open
  }
}
