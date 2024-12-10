import { combineReducers } from "@reduxjs/toolkit";
import authReducer, { AuthState } from '../features/Auth/authSlice'
import loaderReducer, { LoaderState } from "features/loader/loaderReducer";

const createRootReducer = combineReducers({
    auth: authReducer,
    loader: loaderReducer,
})

export interface RootState {
    auth: AuthState;
    loader: LoaderState,
}

export default createRootReducer