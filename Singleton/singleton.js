class DbConnectionSingleton {
  static _instance = null;

  constructor(url, username, password) {
    if (DbConnectionSingleton._instance !== null) {
      console.warn(
        "Use DbConnectionSingleton.getInstance() to create an instance."
      );
    }
    this.url = url;
    this.username = username;
    this.password = password;
  }

  toString() {
    return `[ ${this.url} - ${this.username} - ${this.password} ]`;
  }

  static getInstance(url, username, password) {
    if (DbConnectionSingleton._instance === null) {
      DbConnectionSingleton._instance = new DbConnectionSingleton(
        url,
        username,
        password
      );
    }
    return DbConnectionSingleton._instance;
  }
}

// Example usage:
const dbInstance0 = new DbConnectionSingleton(
  "https://db:120.0.01",
  "username",
  "password"
);
const dbInstance1 = DbConnectionSingleton.getInstance(
  "https://db:120.0.01",
  "username",
  "password"
);
const dbInstance2 = DbConnectionSingleton.getInstance(
  "https://anotherdb:3306",
  "admin",
  "adminpassword"
);

console.log(dbInstance0);
console.log(dbInstance1 === dbInstance2); // This should log true
console.log(dbInstance1, dbInstance2);
