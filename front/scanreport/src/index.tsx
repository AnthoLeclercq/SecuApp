import App from "features/App";
import * as React from "react";
import * as ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import { Provider } from 'react-redux'
import { PersistGate } from "redux-persist/integration/react";
import store, { persistor } from "app/store";
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Loader from "features/loader/Loader";

ReactDOM.render(
  <BrowserRouter>
    <Provider store={store}>
      <PersistGate persistor={persistor}>
        <App />
        <ToastContainer />
        <Loader />
      </PersistGate>
    </Provider>
  </BrowserRouter>,
  document.getElementById("root")
);
