import gql from 'graphql-tag';

export default gql`
  mutation MoveCarExplicit($id: ID, $slotNumber:Int){
    moveCarSlotExplicit(id: $id, slotNumber:$slotNumber){
      car{
        id
        name
        slotNumber
      }
      validationError
    }
  }
`;
