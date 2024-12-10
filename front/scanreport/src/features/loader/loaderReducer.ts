import { SET_LOADER } from './loaderActionTypes';


export interface LoaderState {
  isLoading: boolean;
}

const initialState = {
  isLoading: false,
};

const loaderReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_LOADER:
      return {
        ...state,
        isLoading: action.payload,
      };
    default:
      return state;
  }
};

export default loaderReducer;