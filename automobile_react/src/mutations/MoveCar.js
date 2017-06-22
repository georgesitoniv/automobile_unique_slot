import gql from "graphql-tag";

export default gql`
  mutation MoveCar($carID: ID, $direction: Int){
    moveCarSlot(id: $carID, direction: $direction){
      car{
        id
        name
        slotNumber
      }
    }
  }
`;
