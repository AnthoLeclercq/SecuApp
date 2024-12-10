import { SET_LOADER } from './loaderActionTypes';

export const setLoader = (isLoading: boolean) => ({
  type: SET_LOADER,
  payload: isLoading,
});