import "./styles/styles.css";
import React from "react";
import ReactDOM from "react-dom";
import ApolloClient from "apollo-client";
import { ApolloProvider } from "react-apollo";
import networkInterface from "./apollo/networkInterface";
import injectTapEventPlugin from 'react-tap-event-plugin';
import { createStore, applyMiddleware } from 'redux';

import reducers from './reducers';
import App from "./components/App";

const client = new ApolloClient({
  networkInterface,
  dataIdFromObject: object => object.id
})
const createStoreWithMiddleware = applyMiddleware()(createStore);

injectTapEventPlugin();

const Root = () => {
  return(
    <ApolloProvider store={createStoreWithMiddleware(reducers)} client={client}>
      <App></App>
    </ApolloProvider>
  );
}

ReactDOM.render(<Root/>, document.querySelector("#root"))
