# Automobile
An ambitious attempt to limit the record update to one query. The car models for this project uses a character field for the sorting. 

The Order String:
  
  Format: CarID-BeforeSlotIdentifier-CarID-AfterSlotIdentifier <br/>
  Example: 0000000000000000-9999999999999999-0000000000000000-0000000000000000 <br/>
  
  Implementation:
    Models:
      Car Name: Everest
      Order String: 0000000000000000-9999999999999999-0000000000000001-0000000000000000

      Car Name: Innova
      Order String: 0000000000000000-9999999999999999-0000000000000002-0000000000000000
      
      Car Name: Almera
      Order String: 0000000000000000-9999999999999999-0000000000000003-0000000000000000
    
    
    Actions:
      Move Innova to the front of Everest.
        Process:
        1. Copy the middle CarID of Everest to the middle CarID of Innova
        2. Substract the BeforeSlotIdentifier of the Innova  by 1.
        
        Resulting Sort:
        Car Name: Innova
        Order String: 0000000000000000-9999999999999998-0000000000000001-0000000000000000
        
        Car Name: Everest
        Order String: 0000000000000000-9999999999999999-0000000000000001-0000000000000000
        
      Move Almera to the slot after of Everest.
        Process:
        1. Copy the middle CarID of Everest to the middle CarID of Almera
        2. Add 1 Integer to the the AfterSlotIdentifier of Almera.
        
        Resulting Sort:
        Car Name: Everest
        Order String: 0000000000000000-9999999999999999-0000000000000001-0000000000000000

        Car Name: Almera
        Order String: 0000000000000000-9999999999999999-0000000000000001-0000000000000001
        
