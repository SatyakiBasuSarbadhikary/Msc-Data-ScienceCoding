library(tree)
library(ISLR)
attach(Carseats)

data=select(Carseats,ShelveLoc,Price,Sales)
tree.data1=tree(Sales~.,data)
summary(tree.data1)
plot(tree.data1)
text(tree.data1,pretty=0)
tree.data1

cvtree1=cv.tree(tree.data1,FUN=prune.tree,K=10)
cv.tree(tree.data1)

plot(cv.tree(tree.data1))

plot(cvtree1$k,cvtree1$dev)
#plot(cvtree1$size,cvtree1$dev)









#- `$size`: This vector displays the number of terminal nodes in the pruned trees. It starts with the largest tree size (11) and decreases down to 1, indicating the progression of pruning.

#- `$dev`: This vector shows the deviance values associated with each pruned tree. Deviance represents the goodness of fit of the model, with lower values indicating a better fit to the data. The values decrease as the tree is pruned further.

#- `$k`: This vector provides the complexity parameter (cp) associated with each pruned tree. The complexity parameter controls the trade-off between tree complexity and model accuracy. Smaller values of cp lead to more complex trees, while larger values favor simpler trees. The values shown are in logarithmic scale.

#- `$method`: This indicates the pruning method used, which in this case is "deviance". The deviance method evaluates the goodness of fit by considering the decrease in deviance when a node is split.

#- `attr(,"class")`: This line indicates the class of the object, which is "prune" and "tree.sequence".

