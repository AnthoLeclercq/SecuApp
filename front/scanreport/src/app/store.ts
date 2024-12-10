import { Action, combineReducers, configureStore, ThunkAction } from '@reduxjs/toolkit'
import { createBrowserHistory } from '@remix-run/router'
import authReducer from '../features/Auth/authSlice'
import { FLUSH, PAUSE, PERSIST, persistReducer, persistStore, PURGE, REGISTER, REHYDRATE } from 'redux-persist'
import storage from 'redux-persist/es/storage';
import { RootState } from './rootReducer';
import loaderReducer from 'features/loader/loaderReducer';

export const history = createBrowserHistory();

const persistConfig = {
  key: 'root',
  storage,
}


const rootReducer  = combineReducers({
  auth: authReducer,
  loader: loaderReducer,
})

const persistedReducer = persistReducer(persistConfig, rootReducer)

const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
  getDefaultMiddleware({
    serializableCheck: {
      ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
    },
}),
})



export const persistor = persistStore(store);

export default store

export type AppDispatch = typeof store.dispatch

export type AppThunk = ThunkAction<void, RootState, null, Action<string>>